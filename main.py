import flet as ft

def main(page: ft.Page):
    page.title = "Задание: Счетчик"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    count = 0
    text_hello = ft.Text(value="Нажато: 0 раз", size=25)

    def button_click(e):
        nonlocal count
        count += 1
        text_hello.value = f"Нажато: {count} раз"
        page.update()


    btn = ft.ElevatedButton(text="Кликни сюда", on_click=button_click)

    page.add(text_hello, btn)

ft.app(target=main)
