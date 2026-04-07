import flet as ft 

def main_page(page: ft.Page):
    page.title = 'Мое первое приложение'
    page.theme_mode = ft.ThemeMode.LIGHT
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    greeting_history = []
    favorite_names = []

    greeting_text = ft.Text('История приветствия:')
    favorite_text = ft.Text('Избранные имена:')

    last_name = None  # последнее введённое имя

    def text_name(e):
        nonlocal greeting_history, last_name
        name = text_input.value.strip()

        if name:
            text_hello.value = f"Привет! {name}"
            text_hello.color = ft.Colors.BLUE
            text_input.value = ""

            last_name = name
            greeting_history.append(name)

            # Ограничение до 5 элементов
            greeting_history = greeting_history[-5:]

            greeting_text.value = "История приветствия:\n" + "\n".join(greeting_history)

        else:
            text_hello.value = "Введите корректное имя!" 
            text_hello.color = ft.Colors.RED_900

        page.update()

    def add_to_favorites(e):
        if last_name and last_name not in favorite_names:
            favorite_names.append(last_name)
            favorite_text.value = "Избранные имена:\n" + "\n".join(favorite_names)
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

    text_hello = ft.Text('Как тебя зовут?', size=20)
    text_input = ft.TextField(label='Ваше имя', on_submit=text_name)
    btn = ft.ElevatedButton('send', icon=ft.Icons.SEND, on_click=text_name)

    favorite_btn = ft.ElevatedButton(
        'Добавить в избранное',
        icon=ft.Icons.STAR,
        on_click=add_to_favorites
    )

    theme_btn = ft.IconButton(icon=ft.Icons.BRIGHTNESS_7, on_click=thememode)
    clear_button = ft.IconButton(icon=ft.Icons.DELETE, on_click=clear_history)

    main_object = ft.Row(
        controls=[text_input, btn, clear_button],
        alignment=ft.MainAxisAlignment.CENTER
    ) 

    page.add(
        text_hello,
        main_object,
        favorite_btn,
        theme_btn,
        greeting_text,
        favorite_text
    )

ft.app(main_page, view=ft.AppView.WEB_BROWSER)