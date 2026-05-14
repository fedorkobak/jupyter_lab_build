FROM python:3.14.5-slim

WORKDIR /jlb_package

COPY ./jlb.py jlb.py
COPY ./pyproject.toml pyproject.toml
COPY ./configuration configuration

RUN apt update && apt install -y jq git
RUN pip install .
RUN ./configuration/setup.sh

CMD ["jupyter", "lab", "--ip", "0.0.0.0", "--allow-root"]
