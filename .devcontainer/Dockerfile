# [Choice] Node.js version (use -bookworm, or -bullseye variants on local arm64/Apple Silicon): 20, 18, 20-bookworm, 18-bookworm, 20-bullseye, 18-bullseye, 20-buster, 18-buster
ARG VARIANT=3-bookworm

FROM python:${VARIANT} AS base

ENV DEBIAN_FRONTEND=noninteractive
RUN --mount=type=cache,target=/var/cache/ apt update
RUN --mount=type=cache,target=/var/cache/ apt install sudo -y
RUN --mount=type=cache,target=/var/cache/ apt purge imagemagick imagemagick* -y
RUN --mount=type=cache,target=/var/cache/ apt clean
RUN --mount=type=cache,target=/var/cache/ apt autoremove -y

RUN echo python-user ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/python-user
RUN chmod 0440 /etc/sudoers.d/python-user

FROM base

RUN --mount=type=cache,target=/root/.cache/pip python3 -m pip cache purge > /dev/null 2>&1