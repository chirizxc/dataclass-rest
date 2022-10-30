from typing import Protocol, Any

from dataclass_factory import Factory


class ClientProtocol(Protocol):
    request_body_factory: Factory
    request_args_factory: Factory
    response_body_factory: Factory

    def request(
            self,
            url: str,
            method: str,
            body: Any,
            params: Any,
    ) -> Any:
        raise NotImplementedError


class BaseClient(ClientProtocol):
    def __init__(self):
        self.request_body_factory = self._init_request_body_factory()
        self.request_args_factory = self._init_request_args_factory()
        self.response_body_factory = self._init_response_body_factory()

    def _init_request_body_factory(self) -> Factory:
        return Factory()

    def _init_request_args_factory(self) -> Factory:
        return self.request_body_factory

    def _init_response_body_factory(self) -> Factory:
        return self.request_body_factory
