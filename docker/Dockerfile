FROM python

COPY interface.py /interface.py

RUN pip3 install flask
RUN pip3 install pymysql
RUN pip3 install cryptography

CMD [ "python3", "/interface.py" ]