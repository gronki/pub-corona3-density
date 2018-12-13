#!/usr/bin/env bash

make && ./optest

dvflags='-bf -compton -rel -post'
rm -f d??.dat

BASEPAR=" mdot    0.08
          alpha   0.1"

diskvert $dvflags -o d11 <<EOF
mbh     10
radius  7
${BASEPAR}
EOF

diskvert $dvflags -o d12 <<EOF
mbh     10
radius  70
${BASEPAR}
EOF

diskvert $dvflags -o d81 <<EOF
mbh     1e8
radius  7
${BASEPAR}
EOF

diskvert $dvflags -o d82 <<EOF
mbh     1e8
radius  70
${BASEPAR}
EOF

diskvert $dvflags -o d83 <<EOF
mbh     1e8
radius  400
${BASEPAR}
EOF

parallel diskvert-plot -xl ::: d??.dat
