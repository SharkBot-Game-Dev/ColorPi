#!/bin/bash
set -e

APP_DIR="$(cd "$(dirname "$0")" && pwd)"
RELEASES_DIR="$APP_DIR/releases"
CURRENT_LINK="$APP_DIR/current"
TIMESTAMP=$(date +%Y%m%d_%H%M%S)
NEW_RELEASE_DIR="$RELEASES_DIR/$TIMESTAMP"

echo "🚀 デプロイを開始します: $TIMESTAMP"

mkdir -p "$NEW_RELEASE_DIR"

rsync -av \
  --exclude='node_modules' \
  --exclude='.next' \
  --exclude='releases' \
  --exclude='current' \
  --exclude='.git' \
  "$APP_DIR/" "$NEW_RELEASE_DIR/"

cd "$NEW_RELEASE_DIR"
npm ci
npm run build

rm -f "$CURRENT_LINK"
ln -s "$NEW_RELEASE_DIR" "$CURRENT_LINK"

pm2 reload colorpi-dashboard

cd "$RELEASES_DIR"
ls -1dt */ 2>/dev/null | tail -n +6 | xargs rm -rf 2>/dev/null || true

echo "✅ ゼロダウンタイム更新が完了しました！"