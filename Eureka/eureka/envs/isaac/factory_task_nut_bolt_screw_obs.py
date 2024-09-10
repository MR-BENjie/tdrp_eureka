class FactoryTaskNutBoltScrew(FactoryEnvNutBolt, FactoryABCTask):
    def compute_observations(self):
        """Compute observations."""

        # Shallow copies of tensors
        obs_tensors = [self.fingertip_midpoint_pos,
                       self.fingertip_midpoint_quat,
                       self.fingertip_midpoint_linvel,
                       self.fingertip_midpoint_angvel,
                       self.nut_com_pos,
                       self.nut_com_quat,
                       self.nut_com_linvel,
                       self.nut_com_angvel]

        if self.cfg_task.rl.add_obs_finger_force:
            obs_tensors += [self.left_finger_force, self.right_finger_force]

        obs_tensors = torch.cat(obs_tensors, dim=-1)
        self.obs_buf[:, :obs_tensors.shape[-1]] = obs_tensors  # shape = (num_envs, num_observations)

        return self.obs_buf