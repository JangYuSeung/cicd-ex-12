FROM nginx:1.29.7-alpine

# 설정 파일 및 html/을 컨테이너 내부로 복사
COPY default.conf /etc/nginx/conf.d/default.conf
COPY ./html/ /usr/share/nginx/html/

# COPY ./html/company.html /usr/share/nginx/html/company.html

EXPOSE 80
CMD ["nginx", "-g", "daemon off;"]