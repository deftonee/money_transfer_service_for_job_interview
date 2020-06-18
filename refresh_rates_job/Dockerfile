FROM alpine:3.6

COPY cronjob /etc/crontabs/root

CMD ["crond", "-f", "-d", "8"]
