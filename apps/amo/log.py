from collections import namedtuple

from celery.datastructures import AttributeDict
from tower import ugettext_lazy as _

__all__ = ('LOG', 'LOG_BY_ID', 'LOG_KEEP',)

_LOG = namedtuple('LOG', 'id format')


class CREATE_ADDON:
    id = 1
    format = _(u'{user.name} created addon {addon.name}')
    keep = True


class EDIT_PROPERTIES:
    """ Expects: addon """
    id = 2
    format = _(u'{user.name} edited addon {addon.name} properties')


class EDIT_DESCRIPTIONS:
    id = 3
    format = _(u'{user.name} edited addon {addon.name} description')


class EDIT_CATEGORIES:
    id = 4
    format = _(u'{user.name} edited categories for {addon.name}')


class ADD_USER_WITH_ROLE:
    id = 5
    format = _(u'{user.name} added {0.name} to '
               'addon {addon.name} with role {1}')
    keep = True


class REMOVE_USER_WITH_ROLE:
    id = 6
    # L10n: {0} is the user being removed, {1} is their role.
    format = _(u'{user.name} removed {0} with role {1}')
    keep = True


class EDIT_CONTRIBUTIONS:
    id = 7
    format = _(u'{user.name} edited contributions for {addon.name}')


class SET_INACTIVE:
    id = 8
    format = _(u'{user.name} set addon {addon.name} inactive')
    keep = True


class UNSET_INACTIVE:
    id = 9
    format = _(u'{user.name} activated addon {addon.name}')
    keep = True


class SET_PUBLIC_STATS:
    id = 10
    format = _(u'{user.name} set stats public for {addon}')
    keep = True


class UNSET_PUBLIC_STATS:
    id = 11
    format = _(u'{user.name} set stats private for {addon}')
    keep = True


class CHANGE_STATUS:
    id = 12
    # L10n: {0} is the status
    format = _(u'{user.name} changed {addon} status to {0}')
    keep = True


class ADD_PREVIEW:
    id = 13
    format = _(u'{user.name} added preview to {addon}')


class EDIT_PREVIEW:
    id = 14
    format = _(u'{user.name} edited preview for {addon}')


class DELETE_PREVIEW:
    id = 15
    format = _(u'{user.name} deleted preview from {addon}')


class ADD_VERSION:
    id = 16
    format = _(u'{user.name} added version {0.version} to {addon}')
    keep = True


class EDIT_VERSION:
    id = 17
    format = _(u'{user.name} edited version {0.version} of {addon}')


class DELETE_VERSION:
    id = 18
    format = _(u'{user.name} deleted version {0.version} from {addon}')
    keep = True


class ADD_FILE_TO_VERSION:
    id = 19
    format = _(u'{user.name} added file {0.name} to '
               'version {0.version} of {addon}')


class DELETE_FILE_FROM_VERSION:
    """ Expecting: addon, filename, version

    Because the file is being deleted, filename and version
    should be strings and not the object.
    """
    id = 20
    format = _(u'{user.name} deleted file {0} '
               'from {addon} version {1}')


class APPROVE_VERSION:
    id = 21
    format = _(u'Version {0.version} of {addon} approved')
    keep = True


class RETAIN_VERSION:
    id = 22
    format = _(u'{user.name} retained version {0.version} of {addon}')
    keep = True


class ESCALATE_VERSION:
    id = 23
    # L10n: {0.version} is the version of an addon.
    format = _(u'{user.name} escalated review of {addon} {0.version}')
    keep = True


class REQUEST_VERSION:
    id = 24
    # L10n: {0.version} is the version of an addon.
    format = _(u'{user.name} requested more information regarding '
               '{addon} {0.version}')
    keep = True


class ADD_TAG:
    id = 25
    # L10n: {0} is the tag name.
    format = _(u'{user.name} added tag {0} to {addon}')


class REMOVE_TAG:
    id = 26
    # L10n: {0} is the tag name.
    format = _(u'{user.name} removed tag {0} from {addon}')


class ADD_TO_COLLECTION:
    id = 27
    format = _(u'{user.name} added addon {addon} to a collection {0.name}')


class REMOVE_FROM_COLLECTION:
    id = 28
    forma = _(u'{user.name} removed addon {addon} from a collection {0.name}')


class ADD_REVIEW:
    id = 29
    format = _(u'{user.name} wrote a review about {addon}')


class ADD_RECOMMENDED_CATEGORY:
    id = 31
    # L10n: {0} is a category name.
    format = _(u'{addon} featured in {0}')


class REMOVE_RECOMMENDED_CATEGORY:
    id = 32
    # L10n: {0} is a category name.
    format = _(u'{addon} no longer featured in {0}')


class ADD_RECOMMENDED:
    id = 33
    format = _(u'{addon} is now featured')
    keep = True


class REMOVE_RECOMMENDED:
    id = 34
    format = _(u'{addon} is no longer featured')
    keep = True


class ADD_APPVERSION:
    id = 35
    # L10n: {0} is the application, {1.min/max} is the min/max version of the
    # app
    format = _(u'addon now supports {0} {1.min}-{1.max}')


class CHANGE_USER_WITH_ROLE:
    """ Expects: author.user, role, addon """
    id = 36
    format = _(u'{user.name} changed {0.name} for '
               'addon {addon} with {1}')
    keep = True


class CHANGE_LICENSE:
    """ Expects: license, addon """
    id = 37
    format = _(u'{user.name} changed {addon} to '
               'use license {0.name}')


class CHANGE_POLICY:
    """ Expects: addon """
    id = 38
    format = _(u'{user.name} changed {addon} policy')


class CUSTOM_TEXT:
    id = 98
    format = '{0}'


class CUSTOM_HTML:
    id = 99
    format = '{0}'


LOGS = (CREATE_ADDON, EDIT_PROPERTIES, EDIT_DESCRIPTIONS, EDIT_CATEGORIES,
        ADD_USER_WITH_ROLE, REMOVE_USER_WITH_ROLE, EDIT_CONTRIBUTIONS,
        SET_INACTIVE, UNSET_INACTIVE, SET_PUBLIC_STATS, UNSET_PUBLIC_STATS,
        CHANGE_STATUS, ADD_PREVIEW, EDIT_PREVIEW, DELETE_PREVIEW,
        ADD_VERSION, EDIT_VERSION, DELETE_VERSION, ADD_FILE_TO_VERSION,
        DELETE_FILE_FROM_VERSION, APPROVE_VERSION, RETAIN_VERSION,
        ESCALATE_VERSION, REQUEST_VERSION, ADD_TAG, REMOVE_TAG,
        ADD_TO_COLLECTION, REMOVE_FROM_COLLECTION, ADD_REVIEW,
        ADD_RECOMMENDED_CATEGORY, REMOVE_RECOMMENDED_CATEGORY, ADD_RECOMMENDED,
        REMOVE_RECOMMENDED, ADD_APPVERSION, CUSTOM_TEXT, CUSTOM_HTML,
        CHANGE_USER_WITH_ROLE, CHANGE_LICENSE, CHANGE_POLICY
        )
LOG_BY_ID = dict((l.id, l) for l in LOGS)
LOG = AttributeDict((l.__name__, l) for l in LOGS)
LOG_KEEP = (l.id for l in LOGS if hasattr(l, 'keep'))
