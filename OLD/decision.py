def prompt_decision(options: list[any]):
    """
    Ask the player to choose an option
    """
    formatted_option = '\r\n'.join([f'[{i}] {option}' for i, option in enumerate(options)])
    return input(f"""Choose one of the listed options:
    {formatted_option}
    Your choice: """)
