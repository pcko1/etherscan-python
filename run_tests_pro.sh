#!/bin/bash
clear
export API_PRO_KEY=$1
coverage run -m unittest discover && coverage report -m