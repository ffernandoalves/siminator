```python
class InatorEngine(screen_info: ScreenInfo)
```

Métodos

```python
stop(self, pg_event: pgEvent) -> None
add_callback(self, callback: typing.Tuple[Callable[typing.Concatenate[Args, ...], None]]) -> None
timer(self) -> None
update(self) -> None
start(self) -> None
run(self) -> None
add_models(self, models: typing.List[Drawable]) -> None
renderer(self) -> None
get_callbacks(self) -> None
```