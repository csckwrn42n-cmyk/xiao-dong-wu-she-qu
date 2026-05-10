#!/usr/bin/env python3
import re

with open('/Users/shulan/vibe coding/社区记录小动物/index.html', 'r') as f:
    html = f.read()

# 1. Replace the feed rendering function
old_render = """function renderFriends() {
  const c = document.getElementById('friendsCard');
  c.innerHTML = `<h3>📋 社区动态</h3><div class="fs">看看大家在做什么</div>
    \${state.friendsFeed.map(f => {
      const a = f.animal;
      const comments = [
        {who:'小橘',text:'还行吧……'}, {who:'旺财',text:'哇！好厉害！！'}, {who:'咕咕',text:'嗯，有道理。'}
      ];
      const rc = comments.slice(0, 2 + Math.floor(Math.random()));
      return `<div class="friend-item">
        <div class="fi-header">
          <span class="fi-avatar">\${a.emoji}</span>
          <span class="fi-name">\${a.name}</span>
          <span class="fi-time">\${f.time}</span>
        </div>
        <div class="fi-text">\${f.text}</div>
        <div class="fi-comments">\${rc.map(r => '<div class="fi-comment">' + r.who + '：' + r.text + '</div>').join('')}</div>
      </div>`;
    }).join('')}
    \${state.friendsFeed.length === 0 ? '<div class="report-empty"><div class="re-icon">📭</div>还没有动态呢～去完成一些心愿吧</div>' : ''}</div>`;
}"""

new_render = """function renderFriends() {
  const c = document.getElementById('friendsCard');
  c.innerHTML = `<h3>📋 社区动态</h3><div class="fs">看看大家在做什么</div>
    \${state.friendsFeed.map(f => {
      const a = f.animal;
      const isUser = f.isUser;
      const hasImg = f.imageUrl;
      const cmts = f.comments || [];
      return \`<div class="friend-item" style="\${isUser ? 'background:#fff8f0;border-color:#e8d5b0' : ''}">
        <div class="fi-header">
          <span class="fi-avatar">\${isUser ? '🧑' : a.emoji}</span>
          <span class="fi-name">\${isUser ? '你' : a.name}</span>
          <span class="fi-time">\${f.time}</span>
        </div>
        <div class="fi-text">\${f.text}</div>
        \${hasImg ? '<div class="fi-img" style="text-align:center;padding:4px 0"><img src="' + f.imageUrl + '" style="max-width:90%;max-height:150px;border-radius:8px" onerror="this.style.display=\\'none\\'"></div>' : ''}
        \${cmts.length ? '<div class="fi-comments">' + cmts.map(r => '<div class="fi-comment">' + r.who + '：' + r.text + '</div>').join('') + '</div>' : ''}
      </div>\`;
    }).join('')}
    \${state.friendsFeed.length === 0 ? '<div class="report-empty"><div class="re-icon">📭</div>还没有动态呢～去完成一些心愿吧</div>' : ''}</div>`;
}"""

if old_render in html:
    html = html.replace(old_render, new_render)
    print("renderFriends updated OK")
else:
    print("renderFriends NOT FOUND - checking...")
    idx = html.find("function renderFriends()")
    if idx > -1:
        print(html[idx:idx+100])
    else:
        print("function renderFriends() not found at all!")

# 2. Add collection/gallery JS before the PWA section
old_end = """console.log('\ud83d\udc3e 小动物社区 v1.0 - 双模式 Demo');"""

# Write the file
with open('/Users/shulan/vibe coding/社区记录小动物/index.html', 'w') as f:
    f.write(html)

print("File written")
