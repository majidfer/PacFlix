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
    def __init__(self, data):
        # supaya data bisa diakses dari dalam class User, kita initialize "data" di sini
        self.data = data
        # kita define semua informasi user dengan default value
        self.username = None
        self.current_plan = None
        self.current_duration_plan = 0
        self.referral_code = None

    # buat method untuk set data user
    def set_data(self, username, current_plan, current_duration_plan, referral_code):
        self.username = username
        self.current_plan = current_plan
        self.current_duration_plan = current_duration_plan
        self.referral_code = referral_code

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

    def check_current_plan(self, username):
        for key, value in self.data.items():
            if self.username.lower() == key.lower():
                self.set_data(key, value[0], value[1], value[2])
                print(self.current_plan)
                print(f"{self.current_duration_plan} bulan")
                print(f"\n{self.current_plan} Pacflix Benefit List")
                break

        if self.current_plan == "Basic Plan":
            basic_plan_benefits = [
                ["Services", "Basic Plan"],
                ["Can stream", "True"],
                ["Can download", "True"],
                ["SD", "True"],
                ["HD", "False"],
                ["UHD", "False"],
                ["Number of Devices", 1],
                ["Content", "3rd party movie only"],
                ["Price", 120_000],
            ]
            print(tabulate(basic_plan_benefits, headers="firstrow"), end="")

        elif self.current_plan == "Standard Plan":
            standard_plan_benefits = [
                ["Services", "Standard Plan"],
                ["Can stream", "True"],
                ["Can download", "True"],
                ["SD", "True"],
                ["HD", "True"],
                ["UHD", "False"],
                ["Number of Devices", 2],
                ["Content", "Basic Plan + Sports"],
                ["Price", 160_000],
            ]
            print(
                tabulate(standard_plan_benefits, headers="firstrow"),
                end="",
            )

        elif self.current_plan == "Premium Plan":
            premium_plan_benefits = [
                ["Services", "Premium Plan"],
                ["Can stream", "True"],
                ["Can download", "True"],
                ["SD", "True"],
                ["HD", "True"],
                ["UHD", "True"],
                ["Number of Devices", 4],
                ["Content", "Basic Plan + Standard Plan + Pacflix Original Movies"],
                ["Price", 200_000],
            ]
            print(
                tabulate(premium_plan_benefits, headers="firstrow"),
                end="",
            )

        else:
            print("Plan do not exist!")

    def upgrade_plan(self):
        pass

    def pick_plan(self):
        pass


user_1 = User(data)
user_1.set_data("Shandy", 12, "Basic Plan", "shandy-2134")
user_2 = User(data)
user_2.set_data("Cahya", 24, "Standard Plan", "cahya-abcd")
user_3 = User(data)
user_3.set_data("Ana", 5, "Premium Plan", "ana-2f9g")
user_4 = User(data)
user_4.set_data("Ridho", 1, "No Plan", "ridho-abcd")
# user_1.check_all_plans()
# print("=======================================================")

# user_1.check_current_plan(user_1.username)
user_3.check_current_plan(user_3.username)
