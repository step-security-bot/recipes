ARG VARIANT=3-bullseye

FROM python:${VARIANT} AS base

ENV DEBIAN_FRONTEND=noninteractive
RUN --mount=type=cache,target=/var/cache/ apt update
RUN --mount=type=cache,target=/var/cache/ apt install sudo -y
RUN --mount=type=cache,target=/var/cache/ apt purge imagemagick imagemagick* libcairo2-dev libfreetype6-dev libffi-dev libjpeg-dev libpng-dev libz-dev -y
RUN --mount=type=cache,target=/var/cache/ apt clean
RUN --mount=type=cache,target=/var/cache/ apt autoremove -y

RUN echo python-user ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/python-user
RUN chmod 0440 /etc/sudoers.d/python-user

FROM base

RUN --mount=type=cache,target=/root/.cache/pip python3 -m pip cache purge > /dev/null 2>&1