class FactoryTaskNutBoltPlace(FactoryEnvNutBolt, FactoryABCTask):
    def compute_observations(self):
        """Compute observations."""

        # Shallow copies of tensors
        obs_tensors = [self.fingertip_midpoint_pos,
                       self.fingertip_midpoint_quat,
                       self.fingertip_midpoint_linvel,
                       self.fingertip_midpoint_angvel,
                       self.nut_pos,
                       self.nut_quat,
                       self.bolt_pos,
                       self.bolt_quat]

        if self.cfg_task.rl.add_obs_bolt_tip_pos:
            obs_tensors += [self.bolt_tip_pos_local]

        self.obs_buf = torch.cat(obs_tensors, dim=-1)  # shape = (num_envs, num_observations)

        return self.obs_buf