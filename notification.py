from plyer import notification

title = "Hello World"
message = "Welcome to Python World"

notification.notify(
    title=title,
    message=message,
    app_name="W3schools",
    timeout=10  
)
