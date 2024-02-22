# import library
from tabulate import tabulate

# create dummy data
data = {
    "Shandy": ["Basic Plan", 12, "shandy-2134"],
    "Cahya": ["Standard Plan", 24, "cahya-abcd"],
    "Ana": ["Premium Plan", 5, "ana-2f9g"],
    "Bagus": ["Basic Plan", 11, "bagus-9f92"],
}


# create user class
class User:
    def __init__(self):
        pass

    def check_all_plans(self):
        pacflix_plans_value = [
            ["Services", "Basic Plan", "Standard Plan", "Premium Plan"],
            ["Can stream", "True", "True", "True"],
            [
                "Can download",
                "True",
                "True",
                "True",
            ],
            ["SD", "True", "True", "True"],
            ["HD", "False", "True", "True"],
            ["UHD", "False", "False", "True"],
            ["Number of Devices", 1, 2, 4],
            [
                "Content",
                "3rd party movie only",
                "Basic Plan + Sports",
                "Basic Plan + Standard Plan + Pacflix Original Movies",
            ],
            ["Price", 120_000, 160_000, 200_000],
        ]

        print("Pacflix Plans List:")
        print(tabulate(pacflix_plans_value, headers="firstrow"), end="")

    def check_plan(self, username):
        pass

    def upgrade_plan(self):
        pass

    def pick_plan(self):
        pass


feri = User()
feri.check_all_plans()
