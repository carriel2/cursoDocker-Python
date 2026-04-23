FROM node:20-alpine

LABEL maintainer="Pedro Carriel"

HEALTHCHECK CMD \
    curl --sf http://localhost:5000/ || exit 1

VOLUME [ "/var/nodeapp"]

RUN adduser -h /var/nodeapp \
    -s /bin/bash \
    -D nodeapp && \
    apk add curl

WORKDIR /var/nodeapp

COPY  . . 

RUN chown nodeapp:nodeapp app.js


ARG VERSION
ENV VERSION=${VERSION:-1.0.0}

USER nodeapp
ENTRYPOINT [ "node" ]
CMD [ "app.js" ]
