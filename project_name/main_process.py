#!/usr/bin/env python

from time import sleep

from fertilizer import Fertilizer
from light import Light


def main():
    while True:

        house_list = [1, 2, 3, 4, 5]

        for house_id in house_list:

            print('main')

            fertilizer_result = Fertilizer.process_fertilizer()
            light_result = Light.process_light(house_id=house_id)

            print('fertilizer_result', fertilizer_result)
            print('light_result', light_result)

            Light.switch(1)

        sleep(3)

        print('this is main process')
        print('this is main process from tt')



if __name__ == '__main__':
    main()
