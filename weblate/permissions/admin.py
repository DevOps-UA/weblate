# -*- coding: utf-8 -*-
#
# Copyright © 2012 - 2017 Michal Čihař <michal@cihar.com>
#
# This file is part of Weblate <https://weblate.org/>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from django.contrib import admin
from django.utils.translation import ugettext_lazy as _

from weblate.permissions.models import AutoGroup, GroupACL


class GroupACLAdmin(admin.ModelAdmin):
    list_display = ['language', 'project_subproject', 'group_list']

    def group_list(self, obj):
        groups = obj.groups.values_list('name', flat=True)
        ret = ', '.join(groups[:5])
        if len(groups) > 5:
            ret += ', ...'
        return ret

    def project_subproject(self, obj):
        if obj.subproject:
            return obj.subproject
        else:
            return obj.project
    project_subproject.short_description = _('Project / Component')


class AutoGroupAdmin(admin.ModelAdmin):
    list_display = ('group', 'match')


admin.site.register(GroupACL, GroupACLAdmin)
admin.site.register(AutoGroup, AutoGroupAdmin)
