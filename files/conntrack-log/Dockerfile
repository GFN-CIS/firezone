FROM alpine:latest
RUN apk update
RUN apk add conntrack-tools
RUN rm -fr /var/cache/apk
HEALTHCHECK --interval=1m --timeout=3s \
  CMD pidof conntrack || exit 1
ENTRYPOINT nsenter -t 1 --net conntrack -o timestamp -E -e NEW
