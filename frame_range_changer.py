import bpy


class FrameRangeChanger:
   
    def __init__(self):
        self._old_action_name = self._get_action_name()
    
    def _get_action_name(self):
        obj = bpy.context.object
        ret = (obj.animation_data.action.name
                if obj.animation_data is not None and
                   obj.animation_data.action is not None
                else "")
        return ret

    def handler_changed_action(self, scene, depsgraph):
        new_action_name = self._get_action_name()
        if self._old_action_name != new_action_name:
            scene.frame_start = bpy.data.actions[new_action_name].frame_range[0]
            scene.frame_end = bpy.data.actions[new_action_name].frame_range[1]
        self._old_action_name = new_action_name


frame_range_changer = FrameRangeChanger()
bpy.app.handlers.depsgraph_update_post.append(frame_range_changer.handler_changed_action)