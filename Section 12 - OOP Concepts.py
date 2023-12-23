'''
1.OOP:
    - scalable and reusable

    1.1. Classes: code template for creating a program
    1.2. Objects: based on 1 class we can create many objects
        - instantiation - creating objects
    1.3. Attributes: has (robot.battery_level)
    1.4. Methods(modelled by functions): does (robot.detect_speech), defined as a part of class
'''


class StarCookie:
    milk = 0.1 #class variable

    def __init__(self, color): #initializer
        self.color = color #attribute
        # print('The cookie is ready.')


star_cookie1 = StarCookie('red')
star_cookie1.weight = 14
# star_cookie1.color = 'red'
print(star_cookie1.weight)
print(star_cookie1.color)

star_cookie2 = StarCookie('yellow')
star_cookie2.weight = 16
# star_cookie2.color = 'yellow'
print(star_cookie2.weight)
print(star_cookie2.color)

print(star_cookie1.__dict__)


class Youtube:
    def __init__(self, username, subscribers=0, subscriptions=0): #sets the subscribers by default to zero and there is no need to pass it as an arg when creating obj
        self.username = username
        self.subscribers = subscribers
        self.subscriptions = subscriptions

    def subscribe(self, user):
        user.subscribers += 1
        self.subscriptions += 1

user1 = Youtube('Bogomila')