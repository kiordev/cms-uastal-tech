import flet as ft
import json
from design import *


def main(page: ft.Page):
    page.title = "UASTAL CMS"
    page.window.height = 600
    page.window.width = 1000
    page.window.resizable = False
    page.window.maximizable = False
    page.padding = 0
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    invoice_items = []

    # Верхний текст
    greatingText = ft.Text(
        "СТВОРЕННЯ РАХУНКУ",
        weight=ft.FontWeight.W_700,
        size=35,
        color=prime_color
    )

    # Поля для ввода компании и кода
    companyTextField = ft.TextField(
        label="ТОВ або ФОП",
        hint_text="Название ФОП или ТОВ",
        border_color=prime_color
    )
    codeTextField = ft.TextField(
        label="ЕГРПОУ",
        hint_text="Код ЕГРПОУ",
        border_color=prime_color
    )

    # Поля ввода позиции
    nameField = ft.TextField(label="Назва", width=250)
    qtyField = ft.TextField(label="Кількість", width=100)
    priceField = ft.TextField(label="Ціна з ПДВ", width=150)

    # Таблица с добавленными позициями
    item_table = ft.DataTable(
        columns=[
            ft.DataColumn(ft.Text("Назва")),
            ft.DataColumn(ft.Text("Кількість")),
            ft.DataColumn(ft.Text("Ціна з ПДВ"))
        ],
        rows=[]
    )

    # Обработчик добавления позиции
    def add_item(e):
        name = nameField.value.strip()
        qty = qtyField.value.strip()
        price = priceField.value.strip()

        if name and qty and price:
            invoice_items.append({
                "name": name,
                "quantity": qty,
                "price": price
            })

            item_table.rows.append(
                ft.DataRow(cells=[
                    ft.DataCell(ft.Text(name)),
                    ft.DataCell(ft.Text(qty)),
                    ft.DataCell(ft.Text(price))
                ])
            )
            nameField.value = ""
            qtyField.value = ""
            priceField.value = ""
            page.update()

    # Кнопка "+"
    add_button = ft.IconButton(
        icon=ft.Icons.ADD,
        tooltip="Додати позицію",
        on_click=add_item
    )

    # Ряд с полями ввода позиции
    item_input_row = ft.Row(
        controls=[nameField, qtyField, priceField, add_button],
        alignment=ft.MainAxisAlignment.CENTER
    )

    # Кнопка "Создать счет"
    def create_invoice(e):
        invoice = {
            "company": companyTextField.value.strip(),
            "code": codeTextField.value.strip(),
            "items": invoice_items
        }

        with open("invoice.json", "w", encoding="utf-8") as f:
            json.dump(invoice, f, ensure_ascii=False, indent=4)

        page.snack_bar = ft.SnackBar(ft.Text("✅ Счёт збережено як invoice.json"))
        page.snack_bar.open = True
        page.update()

    create_invoice_button = ft.ElevatedButton(
        text="СТВОРИТИ РАХУНОК",
        on_click=create_invoice,
        bgcolor=prime_color,
        color=white_color
    )

    # Компоновка
    mainInfoRow = ft.Row(
        [companyTextField, codeTextField],
        alignment=ft.MainAxisAlignment.CENTER
    )

    mainColumn = ft.Column(
        [greatingText, mainInfoRow, item_input_row, item_table, create_invoice_button],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        spacing=20
    )

    mainContainer = ft.Container(
        content=mainColumn,
        bgcolor=white_color,
        height=600,
        width=1000
    )

    page.add(mainContainer)


ft.app(main)
