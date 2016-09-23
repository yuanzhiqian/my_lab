local action = ngx.var.request_method;
-- important!  #这里非常重要，一开始我没有添加这行，导致没有成功发出子请求
ngx.req.read_body();

-- get request body
local data = ngx.req.get_body_data();
-- get request uri's args
local args = ngx.req.get_uri_args();

res = ngx.location.capture("/sub2"..ngx.var.request_uri);

ngx.say(res.body);

