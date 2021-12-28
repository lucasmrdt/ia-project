class Shell:
    def select_from_list(list, title="Select an item:"):
        """
        Select an item from a list.
        """
        if len(list) == 0:
            raise ValueError("List is empty")
        if len(list) == 1:
            return list[0]
        for i, item in enumerate(list):
            print(f"{i} - {item}")
        choice = input(f"{title} ")
        try:
            return list[int(choice)]
        except (ValueError, IndexError):
            raise ValueError(f"Invalid choice: {choice}")
