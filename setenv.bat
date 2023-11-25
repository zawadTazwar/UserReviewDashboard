@echo off
for /F "tokens=*" %%A in (sendgrid.env) do (
    set %%A
)