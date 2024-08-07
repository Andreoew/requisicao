import flet as ft

def TextField(hint_text: str, size: int, color: ft.colors, prefix_icon: ft.icons = None, sufix_icon: ft.icons = None, autofocus: bool = False, border: ft.InputBorder = ft.InputBorder.OUTLINE, on_change: ft.ControlEvent = None, password: bool = False, keyboard_type: ft.KeyboardType = None, can_reveal_password = False, bgcolor: ft.colors = ft.colors.WHITE, col: dict = {'sm': 12, 'md': 4}):

  textfield = ft.TextField(
    hint_text=hint_text,
    hint_style=ft.TextStyle(
      size=size,
      weight='bold',
      color=ft.colors.with_opacity(0.2, color)
    ),

    text_style=ft.TextStyle(
      size=size,
      weight='bold',
      color=color
    ),

    prefix_icon=prefix_icon,
    suffix_icon=sufix_icon,
    border=border,
    on_change=on_change,
    password=password,
    autofocus=autofocus,
    keyboard_type=keyboard_type,
    can_reveal_password=can_reveal_password,
    bgcolor=bgcolor,
    col=col
  )

  return textfield

def FloatingButton(bgcolor: ft.colors, text: str = None, icon: ft.icons = None, opacity: ft.OptionalNumber = None , on_click: ft.ControlEvent = None, width: int = None, height: int = None, visible: bool = None, disabled: bool = None, col: dict = {'sm': 12, 'md': 4}):

  floatingbutton = ft.FloatingActionButton(
    bgcolor=bgcolor,
    height=height,
    width=width,
    text=text,
    icon=icon,
    col=col,
    on_click=on_click,
    mouse_cursor=ft.MouseCursor.CLICK,
    visible=visible,
    disabled=disabled,
    opacity=opacity,
  )

  return floatingbutton

def SnackBar(value: str, icon: ft.icons, color: ft.colors):
  
  snackbar = ft.SnackBar(
    content=ft.Row(
      controls=[
        ft.Icon(
          name=icon,
          size=25,
          color=color,
        ),
        
        ft.Text(
          value=value,
          color=color,
          weight='bold',
          size=13
        )
      ]
    )
  )
  
  return snackbar

def IconButton(icon: ft.icons, color: ft.colors, size: int, on_click: ft.ControlEvent = None):
  iconbutton = ft.IconButton(
    icon=icon,
    icon_color=color,
    on_click=on_click,
    icon_size=size
  )
  
  return iconbutton

def AlertDialog(page: ft.Page, title: str, value: str, text_button: str, icon: ft.icons, color: ft.colors, on_click: ft.ControlEvent = None, name: str = None, size: int = None):
  
  def closeMsgbox(e):
    alertadialog.open = False
    
    page.update()
  
  alertadialog = ft.AlertDialog(
    modal=False,
    title=ft.Row(
      controls=[
        ft.Text(
          value=title,
          size=15,
          color=ft.colors.WHITE,
          weight='bold'
        ),
        IconButton(
          icon=ft.icons.CLOSE,
          color=ft.colors.RED,
          size=15,
          on_click=closeMsgbox
        )
      ],
      alignment=ft.MainAxisAlignment.SPACE_BETWEEN
    ),
    content=ft.Row(
      controls=[
        ft.Icon(
          name=name,
          color=color,
          size=size,
        ),
        ft.Text(
          value=value,
          size=13,
          color=color,
          weight='bold'
        )
      ]
    ),
    actions=[
      ft.ElevatedButton(
        text=text_button,
        width=120,
        height=35,
        bgcolor=ft.colors.BLUE,
        on_click=on_click
      )
    ],
    actions_alignment=ft.MainAxisAlignment.END
    
  )
  
  return alertadialog