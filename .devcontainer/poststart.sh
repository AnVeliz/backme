#!/bin/bash

HOST_RESOLV_CONF="/etc/resolv.host.conf"
CONTAINER_RESOLV_CONF="/etc/resolv.conf"
cat "${HOST_RESOLV_CONF}" >> "${CONTAINER_RESOLV_CONF}"

HOST_HOSTS_CONF="/etc/hosts.host"
CONTAINER_HOSTS_CONF="/etc/hosts"
cat "${HOST_HOSTS_CONF}" >> "${CONTAINER_HOSTS_CONF}"