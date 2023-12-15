from itertools import chain

from django.db.models import Model as DjangoModel


def model_to_dict(
    instance: DjangoModel,
    fields=None,
    exclude=None,
    preserve_editable: bool = False,
    preserve_primary_key: bool = False,
) -> dict:
    """
    Monkeypatch of: `django.forms.model_to_dict`
        - to not skip editable=False fields.
        - to add the pk.

    Return a dict containing the data in ``instance`` suitable for passing as
    a Form's ``initial`` keyword argument.

    ``fields`` is an optional list of field names. If provided, return only the
    named.

    ``exclude`` is an optional list of field names. If provided, exclude the
    named from the returned dict, even if they are listed in the ``fields``
    argument.
    """
    opts = instance._meta
    data = {}
    # We also want to include the models pk
    for f in chain(opts.concrete_fields, opts.private_fields, opts.many_to_many):  # type: ignore[attr-defined]
        # ! Monkeypatch: skip editable=False fields
        if not preserve_editable and not getattr(f, "editable", False):
            continue
        if fields is not None and f.name not in fields:
            continue
        if exclude and f.name in exclude:
            continue
        data[f.name] = f.value_from_object(instance)
    # ! Monkeypatch: add pk
    if preserve_primary_key:
        data["pk"] = str(instance.pk)
    return data
