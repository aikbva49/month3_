import flet as ft 

def main_page(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    greeting_history = []

    greeting_text = ft.Text('История приветствия:')

    def text_name(e):
        name = text_input.value.strip()

        if not name:
            text_hello.value = "Введите корректное имя!"
            text_hello.color = ft.Colors.RED

        elif len(name) < 2:
            text_hello.value = "Имя слишком короткое!"
            text_hello.color = ft.Colors.RED

        elif name.isdigit():
            text_hello.value = "Имя не может состоять из цифр!"
            text_hello.color = ft.Colors.RED

        elif name in greeting_history:
            text_hello.value = "Это имя уже в истории!"
            text_hello.color = ft.Colors.RED

        else:
            text_hello.value = f"Привет! {name}"
            text_hello.color = ft.Colors.BLUE

            greeting_history.insert(0, name)

            if len(greeting_history) > 5:
                greeting_history.pop()

            greeting_text.value = "История приветствия:\n" + "\n".join(greeting_history)

        text_input.value = ""
        page.update()

    def thememode(e):
        if page.theme_mode == ft.ThemeMode.DARK:
            page.theme_mode = ft.ThemeMode.LIGHT
        else:
            page.theme_mode = ft.ThemeMode.DARK
        page.update()

    def clear_history(e):
        greeting_history.clear()
        greeting_text.value = "История приветствия:"
        page.update()

    text_hello = ft.Text('Как тебя зовут?', size=24)

    text_input = ft.TextField(
        label='Ваше имя',
        on_submit=text_name
    )

    btn = ft.ElevatedButton(
        'send',
        icon=ft.Icons.SEND,
        on_click=text_name
    )

    theme_btn = ft.IconButton(
        icon=ft.Icons.BRIGHTNESS_7,
        on_click=thememode
    )

    clear_button = ft.IconButton(
        icon=ft.Icons.DELETE,
        on_click=clear_history
    )

    top_row = ft.Row(
        controls=[clear_button, theme_btn],
        alignment=ft.MainAxisAlignment.CENTER
    )

    main_object = ft.Row(
        controls=[text_input, btn],
        alignment=ft.MainAxisAlignment.CENTER
    ) 

    page.add(
        ft.Column(
            [
                top_row,
                text_hello,
                main_object,
                greeting_text
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER
        )
    )

ft.app(main_page, view=ft.AppView.WEB_BROWSER)