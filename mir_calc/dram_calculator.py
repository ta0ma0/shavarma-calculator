import logging
import sys
import argparse


def rur_to_amd(rur_value, rate):
    amd_value = rur_value / float(rate)
    return amd_value

def amd_to_rur(amd_value, rate):
    rur_value = amd_value * float(rate)
    return rur_value


def shavarmator(value, currency):
    if currency == 'RUR':
        price = 200
        return round(float(value) / price, 3)
    if currency == 'AMD':
        price = 950
        return round(float(value) / price, 3)

