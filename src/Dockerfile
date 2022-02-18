FROM public.ecr.aws/lambda/python:3.8 as deps

ARG GITHUB_TOKEN

RUN yum install -y git jq

ADD https://github.com/ZupIT/horusec/releases/download/v2.7.1/horusec_linux_arm64 /usr/bin
RUN chmod +x /usr/bin/horusec_linux_arm64 && mv /usr/bin/horusec_linux_arm64 /usr/bin/horusec
RUN horusec version

COPY requirements.txt .
RUN python3.8 -m pip install -r requirements.txt

COPY . .

# Command can be overwritten by providing a different command in the template directly.
CMD ["handler.lambda_handler"]
