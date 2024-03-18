with open("emails.txt", mode="r") as emails:
    emails_results = emails.read()
    emails_list = emails_results.split()
    for i in range(len(emails_list)):
        if emails_list[i] == "walobwad@gmail.com":
            print(emails_list[i], "found at position", i + 1)
