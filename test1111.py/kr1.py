import flet as ft 

def main_page(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    greeting_history = []
    favorite_names = []

    history_column = ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10
    )
    favorite_column = ft.Column(
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=10
    )

    def update_history_ui():
        history_column.controls.clear()

        for name in greeting_history:
            is_fav = name in favorite_names

            row = ft.Row(
                controls=[
                    ft.Text(name, size=22),
                    ft.IconButton(
                        icon=ft.Icons.STAR if is_fav else ft.Icons.STAR_BORDER,
                        icon_size=28,
                        on_click=lambda e, n=name: toggle_favorite(n)
                    )
                ],
                alignment=ft.MainAxisAlignment.CENTER
            )
            history_column.controls.append(row)

        page.update()

    def update_favorite_ui():
        favorite_column.controls.clear()

        for name in favorite_names:
            favorite_column.controls.append(
                ft.Text(name, size=22)
            )

        page.update()

    def text_name(e):
        name = text_input.value.strip()

        if name:
            text_hello.value = f"Привет! {name}"
            text_hello.color = ft.Colors.BLUE
            text_input.value = ""

            greeting_history.append(name)

            if len(greeting_history) > 5:
                greeting_history.pop(0)

            update_history_ui()

        else:
            text_hello.value = "Введите корректное имя!" 
            text_hello.color = ft.Colors.RED_900

        page.update()

    def toggle_favorite(name):
        if name in favorite_names:
            favorite_names.remove(name)
        else:
            favorite_names.append(name)

        update_history_ui()
        update_favorite_ui()

    def thememode(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK
        
        page.update()

    def clear_history(e):
        greeting_history.clear()
        update_history_ui()

    text_hello = ft.Text('Как тебя зовут?', size=32)

    text_input = ft.TextField(
        label='Ваше имя',
        text_size=20,
        width=300,
        height=60,
        on_submit=text_name
    )

    btn = ft.ElevatedButton(
        'send',
        icon=ft.Icons.SEND,
        scale=1.3,
        on_click=text_name
    )

    clear_button = ft.IconButton(
        icon=ft.Icons.DELETE,
        icon_size=30,
        on_click=clear_history
    )

    theme_btn = ft.IconButton(
        icon=ft.Icons.BRIGHTNESS_7,
        icon_size=30,
        on_click=thememode
    )

    main_row = ft.Row(
        controls=[text_input, btn, clear_button, theme_btn],
        alignment=ft.MainAxisAlignment.CENTER,
        spacing=20
    )



    lists_row = ft.Row(
        controls=[
            ft.Column(
                [ft.Text("Последние:", size=26), history_column],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True
            ),
            ft.Column(
                [ft.Text("Избранные:", size=26), favorite_column],
                horizontal_alignment=ft.CrossAxisAlignment.CENTER,
                expand=True
            )
        ],
        alignment=ft.MainAxisAlignment.CENTER,
        expand=True,
        spacing=50
    )

    page.add(
        ft.Column(
            [
                text_hello,
                main_row,
                lists_row
            ],
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            alignment=ft.MainAxisAlignment.CENTER,
            expand=True,
            spacing=30
        )
    )

ft.app(main_page, view=ft.AppView.WEB_BROWSER)