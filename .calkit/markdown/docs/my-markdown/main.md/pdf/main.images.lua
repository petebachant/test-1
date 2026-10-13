local prefix = "../../../../../../docs/my-markdown"
function Image(el)
  if not el.src:match("^%a[%w+.-]*:") and not el.src:match("^[/#]") then
    el.src = prefix .. "/" .. el.src
  end
  return el
end
