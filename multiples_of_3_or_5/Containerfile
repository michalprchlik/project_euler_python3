FROM alpine
RUN apk update && apk upgrade && apk add --no-cache python3
COPY *.py .
CMD ["application.py"]
ENTRYPOINT ["python3"]