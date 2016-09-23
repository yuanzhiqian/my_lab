local action = ngx.var.request_method;
-- important!  #这里非常重要，一开始我没有添加这行，导致没有成功发出子请求
ngx.req.read_body();

-- get request body
local data = ngx.req.get_body_data();
-- get request uri's args
local args = ngx.req.get_uri_args();

if action == "POST" then
    arry = {method=ngx.HTTP_POST, body=data};
end

-- issue subrequest.
local res1,res2,res3 = ngx.location.capture_multi({
    {"/sub1"..ngx.var.request_uri, {method = ngx.HTTP_POST, body=data}},
    {"/sub2"..ngx.var.request_uri, {method = ngx.HTTP_POST, body=data}},
    {"/sub3"..ngx.var.request_uri, {method = ngx.HTTP_POST, body=data}}
    -- TODO: N's subrequests
})

-- 对返回结果进行业务处理
if res1.status == ngx.HTTP_OK then
    local body = res1.body;
    ngx.say(body);
else
    local body = "Sina:\n"..res1.body.."\nBaidu:\n"..res2.body.."\nBing:\n"..res3.body;
    ngx.say(body);
end
