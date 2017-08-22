#!/bin/sh
  
  cp $BASE_DIR/../custom-scripts/S41network-config $BASE_DIR/target/etc/init.d
  chmod +x $BASE_DIR/target/etc/init.d/S41network-config

  cp $BASE_DIR/../custom-scripts/web-server.py $BASE_DIR/target/etc
  chmod +x $BASE_DIR/target/etc/web-server.py
  
  cp $BASE_DIR/../custom-scripts/index.html $BASE_DIR/target/etc
  
  cp $BASE_DIR/../custom-scripts/Sweb-server-config $BASE_DIR/target/etc/init.d
  chmod +x $BASE_DIR/target/etc/init.d/Sweb-server-config
