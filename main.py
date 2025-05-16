# UASTAL CMS SYSTEM
# 16/05/2025
# Kior Oleksandr Sergyovich

import flet as ft
from design import *

def main(page: ft.Page):

    # Page Settings
    page.title = "UASTAL CMS"
    page.window.height = 600
    page.window.width = 1000
    page.window.resizable = False
    page.window.maximizable = False
    page.padding = 0
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    #USER INTERFACE
    # Основные кнопки
    createInvoiceButton = ft.FilledButton(
        content=ft.Row([
            ft.Text("СТВОРИТИ", color=white_color),
            ft.Icon(name=ft.Icons.ADD, color=white_color)],
            alignment=ft.MainAxisAlignment.CENTER
            ),
        bgcolor=prime_color,
        )
    
    editInvoiceButton = ft.FilledButton(
        content=ft.Row([
            ft.Text("РЕДАГУВАТИ", color=white_color),
            ft.Icon(name=ft.Icons.EDIT, color=white_color)],
            alignment=ft.MainAxisAlignment.CENTER
            ),
        bgcolor=prime_color,
        )
    
    exportRAHInvoiceButton = ft.FilledButton(
        content=ft.Row([
            ft.Text("РАХУНОК PDF", color=white_color),
            ft.Icon(name=ft.Icons.CREDIT_CARD, color=white_color)],
            alignment=ft.MainAxisAlignment.CENTER
            ),
        bgcolor=prime_color,
        )
    
    exportVIDInvoiceButton = ft.FilledButton(
        content=ft.Row([
            ft.Text("ВИДАТКОВА PDF", color=white_color),
            ft.Icon(name=ft.Icons.CREDIT_CARD, color=white_color)],
            alignment=ft.MainAxisAlignment.CENTER
            ),
        bgcolor=prime_color,
        )
    
    # Текст
    greatingText = ft.Text(
        "UASTAL CMS SYSTEM", 
        weight=ft.FontWeight.W_700, 
        size=35, 
        color=prime_color)
    
    tipText = ft.Text(
        "Система обліку і створення документів",
        weight=ft.FontWeight.W_500, 
        size=15,
        color=prime_color)
    
    # Layout
    # Ряд с кнопками
    buttonRow = ft.Row([
        createInvoiceButton, 
        editInvoiceButton, 
        exportRAHInvoiceButton, 
        exportVIDInvoiceButton],
        alignment=ft.MainAxisAlignment.SPACE_AROUND
        )
    
    # Основная колонка
    mainColumn = ft.Column([
        greatingText, 
        tipText,
        buttonRow],
        alignment=ft.MainAxisAlignment.START,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        )
    
    # Главный контейнер
    mainContainer = ft.Container(
        content=mainColumn,
        bgcolor=white_color,
        height=600,
        width=1000,
    )

    page.add(mainContainer)

ft.app(main)