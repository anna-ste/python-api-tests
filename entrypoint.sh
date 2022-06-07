#!/bin/bash -e

behave -f allure -o reports -f pretty

/tests/allure-2.13.8/bin/allure serve --port 8080 reports