Name     : golang-github-gorilla-websocket
Version  : 0
Release  : 3
URL      : https://github.com/gorilla/websocket/archive/39cd638460acf1c01aaac38effc6e54ee7e04bca.tar.gz
Source0  : https://github.com/gorilla/websocket/archive/39cd638460acf1c01aaac38effc6e54ee7e04bca.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : BSD-2-Clause
BuildRequires: go

%description
# Gorilla WebSocket
Gorilla WebSocket is a [Go](http://golang.org/) implementation of the
[WebSocket](http://www.rfc-editor.org/rfc/rfc6455.txt) protocol.

%prep
%setup -q -n websocket-39cd638460acf1c01aaac38effc6e54ee7e04bca

%build

%install
gopath="/usr/lib/golang"
library_path="github.com/gorilla/websocket"
rm -rf %{buildroot}
install -d -p %{buildroot}${gopath}/src/${library_path}/
for file in $(find . -iname "*.go") ; do
     install -d -p %{buildroot}${gopath}/src/${library_path}/$(dirname $file)
     cp -pav $file %{buildroot}${gopath}/src/${library_path}/$file
done

%check
export GOPATH=%{buildroot}${gopath}
go test ${library_path}

%files
%defattr(-,root,root,-)
/usr/lib/golang/src/github.com/gorilla/websocket/bench_test.go
/usr/lib/golang/src/github.com/gorilla/websocket/client.go
/usr/lib/golang/src/github.com/gorilla/websocket/client_server_test.go
/usr/lib/golang/src/github.com/gorilla/websocket/client_test.go
/usr/lib/golang/src/github.com/gorilla/websocket/conn.go
/usr/lib/golang/src/github.com/gorilla/websocket/conn_test.go
/usr/lib/golang/src/github.com/gorilla/websocket/doc.go
/usr/lib/golang/src/github.com/gorilla/websocket/examples/autobahn/server.go
/usr/lib/golang/src/github.com/gorilla/websocket/examples/chat/conn.go
/usr/lib/golang/src/github.com/gorilla/websocket/examples/chat/hub.go
/usr/lib/golang/src/github.com/gorilla/websocket/examples/chat/main.go
/usr/lib/golang/src/github.com/gorilla/websocket/examples/filewatch/main.go
/usr/lib/golang/src/github.com/gorilla/websocket/json.go
/usr/lib/golang/src/github.com/gorilla/websocket/json_test.go
/usr/lib/golang/src/github.com/gorilla/websocket/server.go
/usr/lib/golang/src/github.com/gorilla/websocket/server_test.go
/usr/lib/golang/src/github.com/gorilla/websocket/util.go
/usr/lib/golang/src/github.com/gorilla/websocket/util_test.go
