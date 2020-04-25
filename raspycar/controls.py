import logging
from enum import Enum

from gpiozero import PWMOutputDevice, exc

logger = logging.getLogger(__file__)


class Pins(Enum):
    FORWARD_LEFT = 18
    FORWARD_RIGHT = 27
    REVERSE_LEFT = 24
    REVERSE_RIGHT = 10


class Throttle(Enum):
    NONE = 0.0
    FULL = 1.0


try:
    pwm_forward_left = PWMOutputDevice(Pins.FORWARD_LEFT.value, True, 0, 1000)
    pwm_reverse_left = PWMOutputDevice(Pins.REVERSE_LEFT.value, True, 0, 1000)

    pwm_forward_right = PWMOutputDevice(Pins.FORWARD_RIGHT.value, True, 0, 1000)
    pwm_reverse_right = PWMOutputDevice(Pins.REVERSE_RIGHT.value, True, 0, 1000)

    def stop():
        """Stop all motion"""
        pwm_forward_left.value = Throttle.NONE.value
        pwm_reverse_left.value = Throttle.NONE.value
        pwm_forward_right.value = Throttle.NONE.value
        pwm_reverse_right.value = Throttle.NONE.value

    def forward():
        """Go forwards"""
        pwm_forward_left.value = Throttle.FULL.value
        pwm_reverse_left.value = Throttle.NONE.value
        pwm_forward_right.value = Throttle.FULL.value
        pwm_reverse_right.value = Throttle.NONE.value

    def reverse():
        """Go backwards"""
        pwm_forward_left.value = Throttle.NONE.value
        pwm_reverse_left.value = Throttle.FULL.value
        pwm_forward_right.value = Throttle.NONE.value
        pwm_reverse_right.value = Throttle.FULL.value

    def left():
        """Spin the car left"""
        pwm_forward_left.value = Throttle.NONE.value
        pwm_reverse_left.value = Throttle.NONE.value
        pwm_forward_right.value = Throttle.FULL.value
        pwm_reverse_right.value = Throttle.NONE.value

    def right():
        """Spin the car right"""
        pwm_forward_left.value = Throttle.FULL.value
        pwm_reverse_left.value = Throttle.NONE.value
        pwm_forward_right.value = Throttle.NONE.value
        pwm_reverse_right.value = Throttle.NONE.value


except exc.BadPinFactory:
    logger.error("Unable to use pins, controls will not work!")

    def stop():
        logger.error('"stop" called')

    def forward():
        logger.error('"forward" called')

    def reverse():
        logger.error('"reverse" called')

    def left():
        logger.error('"left" called')

    def right():
        logger.error('"right" called')
