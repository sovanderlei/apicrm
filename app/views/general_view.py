import io

import pandas as pd
from fastapi import APIRouter, Depends, Response
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from app.database.db import get_db

router = APIRouter()

@router.get("/general/hello")
async def hello_world():
    return {"message": "Olá, Mundo!"}

@router.get("/general/status")
async def system_status():
    return {
        "status": "running",
        "database": "connected",
        "version": "1.0.0"
    }

@router.get("/general/db-check")
async def check_database(db: Session = Depends(get_db)):
    try:
        db.execute("SELECT 1")
        return {"database": "Connected"}
    except Exception as e:
        return {"database": "Error", "details": str(e)}

@router.get("/general/export-sales") 
async def export_sales():
    data = [
        {"Item": 1, "Nome do Produto": "Produto A", "Data Venda": "2025-03-15", "Quantidade": 2, "Valor Unitário": 10.0, "Total": 20.0},
        {"Item": 2, "Nome do Produto": "Produto B", "Data Venda": "2025-03-15", "Quantidade": 5, "Valor Unitário": 15.0, "Total": 75.0},
        {"Item": 3, "Nome do Produto": "Produto C", "Data Venda": "2025-03-15", "Quantidade": 1, "Valor Unitário": 50.0, "Total": 50.0},
        {"Item": 4, "Nome do Produto": "Produto D", "Data Venda": "2025-03-15", "Quantidade": 3, "Valor Unitário": 20.0, "Total": 60.0},
        {"Item": 5, "Nome do Produto": "Produto D", "Data Venda": "2025-03-15", "Quantidade": 4, "Valor Unitário": 25.0, "Total": 100.0},
        {"Item": 6, "Nome do Produto": "Produto C", "Data Venda": "2025-03-15", "Quantidade": 2, "Valor Unitário": 30.0, "Total": 60.0},
        {"Item": 7, "Nome do Produto": "Produto B", "Data Venda": "2025-03-15", "Quantidade": 6, "Valor Unitário": 12.0, "Total": 72.0},
        {"Item": 8, "Nome do Produto": "Produto A", "Data Venda": "2025-03-15", "Quantidade": 7, "Valor Unitário": 8.0, "Total": 56.0},
        {"Item": 9, "Nome do Produto": "Produto B", "Data Venda": "2025-03-15", "Quantidade": 3, "Valor Unitário": 40.0, "Total": 120.0},
        {"Item": 10, "Nome do Produto": "Produto A", "Data Venda": "2025-03-15", "Quantidade": 5, "Valor Unitário": 18.0, "Total": 90.0},
    ]
    
    df = pd.DataFrame(data)
    total_geral = df["Total"].sum()
    
    df.loc[len(df.index)] = ["", "TOTAL GERAL", "", "", "", total_geral]

    grouped = df.groupby("Nome do Produto")["Total"].sum()

    output = io.BytesIO()
    with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
        df.to_excel(writer, index=False, sheet_name="Vendas")

        workbook = writer.book
        worksheet = writer.sheets["Vendas"]
        
        header_format = workbook.add_format({'bg_color': '#D3D3D3', 'bold': True, 'align': 'center', 'valign': 'vcenter', 'border': 1})
        total_format = workbook.add_format({'bg_color': '#D3D3D3', 'bold': True, 'align': 'center', 'valign': 'vcenter', 'border': 1})
        zebra_format_odd = workbook.add_format({'bg_color': '#F2F2F2', 'border': 1})
        zebra_format_even = workbook.add_format({'bg_color': '#FFFFFF', 'border': 1})

        for col_num, value in enumerate(df.columns.values):
            worksheet.write(0, col_num, value, header_format)
        
        for row_num, row in df.iterrows():
            for col_num in range(len(df.columns)):
                if row_num % 2 == 0:
                    worksheet.write(row_num + 1, col_num, row.iloc[col_num], zebra_format_even)
                else:
                    worksheet.write(row_num + 1, col_num, row.iloc[col_num], zebra_format_odd)

        total_row = len(df)
        for col_num in range(len(df.columns)):
            worksheet.write(total_row, col_num, df.iloc[total_row - 1, col_num], total_format)

        for row_num in range(1, len(df) + 1):
            for col_num in range(6):
                if pd.notna(df.iloc[row_num - 1, col_num]):
                    worksheet.write(row_num, col_num, df.iloc[row_num - 1, col_num], header_format if row_num == 0 else zebra_format_even if row_num % 2 == 0 else zebra_format_odd)

        worksheet.set_column('A:F', 20)

        chart = workbook.add_chart({'type': 'pie'})

        chart.add_series({
            'name': 'Vendas por Produto',
            'categories': f'=Vendas!$B$2:$B${len(grouped)+1}',
            'values': f'=Vendas!$F$2:$F${len(grouped)+1}',
        })

        worksheet.insert_chart('H2', chart)

    output.seek(0)
    
    headers = {
        "Content-Disposition": "attachment; filename=sales_report_with_pie_chart.xlsx",
        "Content-Type": "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
    }

    return StreamingResponse(output, headers=headers)

