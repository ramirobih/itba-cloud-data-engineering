#!/bin/bash

PGPASSWORD=password psql -h localhost -U user -d flights -a -f create_tables.sql