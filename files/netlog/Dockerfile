FROM alpine:latest
RUN apk update
RUN apk add conntrack-tools
RUN rm -fr /var/cache/apk
ENTRYPOINT nsenter -t 1 --net conntrack -o timestamp -E -e NEW
