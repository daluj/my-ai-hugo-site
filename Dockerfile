FROM klakegg/hugo:ext-alpine AS builder

WORKDIR /app

# Copy project files
COPY . /app

# Install dependencies (if needed)
RUN apk add --no-cache nodejs npm && \
    npm install -g postcss-cli autoprefixer tailwindcss

# Build the Hugo site
RUN hugo --minify

# Final production image
FROM nginx:alpine

COPY --from=builder /app/public /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]