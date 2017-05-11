#!/bin/bash

mpstat -I SCPU |awk '{printf "%s %-3s %-10s %-10s\n",$1,$2,$5,$6}'

