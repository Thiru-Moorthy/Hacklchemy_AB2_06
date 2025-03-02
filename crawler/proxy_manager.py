from stem import Signal
from stem.control import Controller

# Change TOR IP Address
def renew_tor_ip():
    with Controller.from_port(port=9051) as controller:
        controller.authenticate(password='your_password')  # Change this!
        controller.signal(Signal.NEWNYM)

if __name__ == "__main__":
    renew_tor_ip()
